REST_FRAMEWORK ={
    'DEFAULT_PAGINATION_CLASS':"rest_framework.pagination.PageNumberPagination",
    'PAGE_SIZE':5
}

#EMAIL SMTP 

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "patildevesh677@gmail.com"
EMAIL_HOST_PASSWORD = "XYZ"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER