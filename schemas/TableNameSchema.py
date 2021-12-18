from pydantic import BaseModel


class TableNameSchema(BaseModel):
    """
    Schema of database table name
    """

    residence_address = "ResidenceAddress"
    residence_values = ("ResidenceValues",)
    residence_features = ("ResidenceFeatures",)
    residence = "Residence"
