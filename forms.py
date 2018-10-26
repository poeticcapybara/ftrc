import wtforms_json
from wtforms import FloatField, Form
from wtforms.validators import required, NumberRange

wtforms_json.init()


class PredictionParametersForm(Form):
    crime_rate = FloatField('crime_rate', validators=[required(),
        NumberRange(min=0, message='crime_rate should be greater or equal to %(min)s')])
    avg_number_of_rooms = FloatField('avg_number_of_rooms', validators=[required(),
        NumberRange(min=0, message='avg_number_of_rooms should be greater or equal to %(min)s')])
    distance_to_employment_centers = FloatField('distance_to_employment_centers', validators=[required(),
        NumberRange(min=0, message='distance_to_employment_centers should be greater or equal to %(min)s')])
    property_tax_rate = FloatField('property_tax_rate', validators=[required(),
        NumberRange(min=0, message='property_tax_rate should be greater or equal to %(min)s')])
    pupil_teacher_ratio = FloatField('pupil_teacher_ratio', validators=[required(),
        NumberRange(min=0, message='pupil_teacher_ratio should be greater or equal to %(min)s')])
