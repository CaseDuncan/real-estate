from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _ 


class CustomUserManager(BaseUserManager):
    def email_validation(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Valid email address must be provided"))

    def create_user(self, username,first_name, last_name, email, password, **extrafields):
        if not username:
            raise ValueError(_("username is required"))

        if not first_name:
            raise ValueError(_("firstname is required"))

        if not last_name:
            raise ValueError(_("lastname is required"))

        if email:
            email = self.normalize_email(email)
            self.email_validation(email)
        else:
          raise ValueError(_("valid email is required"))

        user = self.model(
            username = username, 
            first_name = first_name,
            last_name = last_name,
            email = email,
            **extrafields
        )

        user.set_password(password)
        extrafields.setdefault("is_staff", False)
        extrafields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(username, first_name, last_name, password,**extrafields):
        extrafields.setdefault("super_user", True)
        extrafields.setdefault("is_staff",True)
        extrafields.setdefault("is_active",True)

        if extrafields.get("is_superuser") is not True:
            raise ValueError(_("superusers must have is_superuser=True"))
        
        if extrafields.get("is_staff") is not True:
           raise ValueError(_("superusers must have is_staff=True"))

        if extrafields.get("is_active") is not True:
            raise ValueError(_("superusers must have is_active=True"))
        if not password:
            raise ValueError(_("a superuser must have a password"))
        
        if email:
            email.normalize_email(email)
            self.email_validation(email)
        else:
          raise ValueError(_("superusers must provide valid email address"))

        user = self.create_user(username, first_name, last_name, email, password)

        user.save(using=self._db)
        return user
            
