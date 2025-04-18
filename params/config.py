from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MAIN_EXCEL_FILE_PATH: Optional[str]
    MAIN_FOLDER_PATH: Optional[str]
    DIABETIC_FOOT: Optional[str]
    DIABETIC_KIDNEY_DISEASE: Optional[str]
    NEUROENDOCRINOLOGY: Optional[str]
    ENDOCRINOPATHIES_THERAPY: Optional[str]
    PATHOLOGY_OF_PARATHYROID_GLANDS: Optional[str]
    ANESTHESIOLOGY_AND_RESUSCITATION_CENTER: Optional[str]
    CARDIOLOGY_AND_VASCULAR_SURGERY: Optional[str]
    ENDOCRINOPATHIES_OF_EARLY_AGE: Optional[str]
    ANDROLOGY_AND_UROLOGY: Optional[str]
    DIABETES_FORECASTING_AND_INNOVATION: Optional[str]
    SURGERY: Optional[str]
    ASSISTED_REPRODUCTIVE_TECHNOLOGIES: Optional[str]
    THYROID_GLAND: Optional[str]
    CHILDHOOD_ENDOCRINE_TUMORS: Optional[str]
    PEDIATRIC_SURGERY: Optional[str]
    CHILDHOOD_DIABETES_MELLITUS: Optional[str]
    OSTEOPOROSIS_AND_OSTEOPATHY: Optional[str]
    PEDIATRIC_THYROIDOLOGY: Optional[str]

    class Config:
        env_file = '.env'


settings = Settings()
