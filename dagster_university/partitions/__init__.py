from dagster import MonthlyPartitionsDefinition, WeeklyPartitionsDefinition
from ..assets import constants

start_date = constants.START_DATE
end_date = constants.END_DATE

monthly_partitions = MonthlyPartitionsDefinition(
    start_date=start_date,
    end_date=end_date,
)

weekly_partitions = WeeklyPartitionsDefinition(
    start_date=start_date,
    end_date=end_date
)