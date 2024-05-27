# E_commerce_django

## Custom admin dashboard using jazzmin
    + pip install django-jazzmin
    + Link : https://django-jazzmin.readthedocs.io/configuration/
## Config admin (superuser)
    + Tạo 1 apps có models kết thừa abstractuser
    + AUTH_USER_MODEL = '' trong settings để đặt lớp models tuỳ chỉnh  
    + comment contrib.admin lại
    + Thực hiện makemigrations để tạo migration và migrate nó
    => Các trường trong admin sẽ được cập nhật tuỳ chỉnh