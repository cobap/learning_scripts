# %%


from create_report import create_report
from prefect import flow

# Data Pipelines
# https://towardsdatascience.com/create-robust-data-pipelines-with-prefect-docker-and-github-12b231ca6ed2
# https://towardsdatascience.com/create-a-maintainable-data-pipeline-with-prefect-and-dvc-1d691ea5bcea

# %%

from pytrends.request import TrendReq
from prefect import flow, task
import plotly.express as px
import datapane as dp

import datapane as dp
from prefect import flow, task
from prefect_shell import shell_run_command
from prefect.blocks.system import Secret


@task
def get_dp_token():
    secret_block = Secret.load("datapane-token")

    # Access the stored secret
    return secret_block.get()


@flow
def login_into_datapane():
    token = get_dp_token()
    return shell_run_command(f"datapane login --token {token}")


@task
def upload_report(report_elements: list, keyword: str):
    dp.Report(*report_elements).upload(
        name=f"{keyword.title()} Report", publicly_visible=True
    )


@flow(name="Create a Report")
def create_report(report_elements: list, keyword: str):
    login_into_datapane()
    upload_report(report_elements, keyword)


@task(retries=3, retry_delay_seconds=10)
def get_pytrends(keyword: str):
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload([keyword])
    return pytrends


@task
def get_interest_overtime(pytrends: TrendReq, keyword: str, start_date: str):
    df = pytrends.interest_over_time().loc[start_date:]
    fig = px.line(data_frame=df[keyword])
    return [dp.Text("# Interest Overtime"), dp.Plot(fig)]


@task
def get_interest_by_region(pytrends: TrendReq, keyword: str, num_countries: int):
    country = pytrends.interest_by_region(
        resolution="COUNTRY", inc_low_vol=True, inc_geo_code=False
    ).sort_values(by=keyword, ascending=False)
    fig = px.bar(data_frame=country[:num_countries])
    return [dp.Text("# Interest by Countries"), dp.Plot(fig)]


@task
def get_related_queries(pytrends: TrendReq, keyword: str):
    df = pytrends.related_queries()[keyword]["top"]
    fig = px.bar(data_frame=df, x="query", y="value")
    return [dp.Text(f"# Related Queries to {keyword}"), dp.Plot(fig)]


@flow(name="Get Google Trends for a Keyword")
def get_keywords_stats(keyword: str, start_date: str, num_countries: int):
    """Get statistics of a keyword on Google Trends"""
    pytrends = get_pytrends(keyword)
    interest_over_time = get_interest_overtime(pytrends, keyword, start_date)
    interest_by_region = get_interest_by_region(
        pytrends, keyword, num_countries)
    related_queries = get_related_queries(pytrends, keyword)
    return [*interest_over_time, *interest_by_region, *related_queries]


if __name__ == "__main__":
    keyword = "COVID"
    start_date = "2020-01-01"
    num_countries = 10
    get_keywords_stats(keyword, start_date, num_countries)


@flow(name="Create a Report for Google Trends")
def create_pytrends_report(
    keyword: str = "COVID", start_date: str = "2020-01-01", num_countries: int = 10
):
    report_components = get_keywords_stats(keyword, start_date, num_countries)
    create_report(report_components, keyword)


if __name__ == "__main__":
    create_pytrends_report()
