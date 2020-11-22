# Web Application Base v0.1.0

Este proyecto es una API que permite administrar posts y users de un blog usando Docker, docker-compose, python(django) y postgres; teniendo en cuenta las mejores prácticas([12factor](https://12factor.net/)) en un ambiente de desarrollo hasta su despliegue en producción(DO, AWS).


# How to install?

```
make install
make migrate
make loaddata
```

> loaddata: Create an admin user with email 'victor@yopmail.com' and password 'admin'.


# How to start?

```
make start
```

# How to stop?

```
make stop
```

# How to use the API?

> **Request tools:** Httpie, Postman, Insomnia.

```
http POST localhost:8000/users/login/ email=victor@admin.com password=admin12345
```

```
http POST localhost:8000/users/signup/ email=victor@admin.com first_name=Victor last_name=Alo password=admin12345 password_confirmation=admin12345 username=victor
```

# Additional commands

```
new
status
fix
purge
logs
```

```
django
makemigrations
migrate
createsuperuser
loaddata
```

# Notes

```
import pdb; pdb.set_trace()
```