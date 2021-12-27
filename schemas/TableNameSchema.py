from pydantic import BaseModel


class TableNameSchema(BaseModel):
    """Schema of database table name"""

    residence_address = "residenceAddress"
    residence_values = "residenceValues"
    residence_features = "residenceFeatures"
    residence = "residence"
