import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.tables import dash_ag_grid

df = px.data.gapminder()

columnDefs = [{"field": "country"}, {"field": "year"}, {"field": "lifeExp", "cellDataType": "numeric"},
              {"field": "gdpPercap", "cellDataType": "dollar"}, {"field": "pop", "cellDataType": "numeric"}]

page = vm.Page(
    title="Example of AG Grid with formatted columns",
    components=[
        vm.AgGrid(
            title="AG Grid with formatted columns",
            figure=dash_ag_grid(
                data_frame=df,
                columnDefs=columnDefs,
            ),
        )
    ],
)

dashboard = vm.Dashboard(pages=[page])

Vizro().build(dashboard).run()