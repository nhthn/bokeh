''' A scatter plot that demonstrates different ways of adding labels.

.. bokeh-example-metadata::
    :apis: bokeh.models.ColumnDataSource, bokeh.models.Label, bokeh.models.LabelSet bokeh.plotting.figure.scatter
    :refs: :ref:`ug_basic_annotations_labels`
    :keywords: scatter, label

'''

from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.plotting import figure, show

source = ColumnDataSource(data=dict(
    height=[66, 71, 72, 68, 58, 62],
    weight=[165, 189, 220, 141, 260, 174],
    names=['Mark', 'Amir', 'Matt', 'Greg', 'Owen', 'Juan']
))

p = figure(title='Dist. of 10th Grade Students', x_range=(140, 275))
p.xaxis.axis_label = 'Weight (lbs)'
p.yaxis.axis_label = 'Height (in)'

p.scatter(x='weight', y='height', size=8, source=source)

labels = LabelSet(x='weight', y='height', text='names',
                  x_offset=5, y_offset=5, source=source)

citation = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text='Collected by Luke C. 2016-04-01',
                 border_line_color='black', background_fill_color='white')

p.add_layout(labels)
p.add_layout(citation)

show(p)
