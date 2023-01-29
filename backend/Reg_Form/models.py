from django.db import models



# Create your models here.


# class Aero_Eng(models.Model):
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     Registration_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default= False)

# class Civil_Eng(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     Registration_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default= False)


# class Cse_Eng(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     Registration_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default= False)


# class Ece_Eng(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     Registration_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default= False)

    
# class Mech_Eng(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     Registration_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)

# class Bio_Eng(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     Registration_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)


# class Design(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)

# class ISBJ(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)

# class Management(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)


# class Vedic_Science(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     selection = models.BooleanField(default = False)
#     event_name = models.CharField(max_length=50)
#     Registration_name = models.CharField(max_length=50)

# class School_of_Education_and_Research (models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)

# class SOFA(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)


# class SFT(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)
    

# class Architecture_Eng(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)

# class Culture(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)
        
# class FoodAndTechnology(models.Model):#1
#     auto_increment_id = models.AutoField(primary_key=True)
#     event_name = models.CharField(max_length=50)
#     selection = models.BooleanField(default = False)
#     Registration_name = models.CharField(max_length=50)

class users(models.Model):
    id = models.BigAutoField(primary_key=True)
    Fullname = models.CharField(max_length=20)    
    email = models.EmailField(max_length=20)
    College = models.CharField(max_length=20)    
    PhoneNo = models.CharField(max_length=10)
    event = models.CharField(max_length=50)
    # Txn_id = models.CharField(max_length=100)
    # timestamp = models.CharField(max_length=20)

class admin_data(models.Model):
    id = models.CharField(max_length=50 ,primary_key=True)
    Fullname = models.CharField(max_length=20)    
    email = models.EmailField(max_length=20)
    College = models.CharField(max_length=20)    
    PhoneNo = models.CharField(max_length=10)
    event = models.CharField(max_length=50)
    Txn_id = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=20)


   
