import plotly.express as px
import pandas as pd

df = pd.DataFrame(
    [
        dict(Task="Project Planning", Start="2025-01-01", Finish="2025-01-10"),
        dict(Task="Development", Start="2025-01-11", Finish="2025-02-15"),
        dict(Task="Testing", Start="2025-02-16", Finish="2025-03-01"),
        dict(Task="Launch", Start="2025-03-05", Finish="2025-03-10"),
    ]
)

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")

fig.update_yaxes(autorange="reversed")
fig.show()
