from dbt.adapters.doris.connections import DorisConnectionManager
from dbt.adapters.doris.connections import DorisCredentials
from dbt.adapters.doris.relation import DorisRelation
from dbt.adapters.doris.column import DorisColumn
from dbt.adapters.doris.impl import DorisAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import doris


Plugin = AdapterPlugin(
    adapter=DorisAdapter,
    credentials=DorisCredentials,
    include_path=doris.PACKAGE_PATH)
