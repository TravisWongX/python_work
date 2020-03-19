from administrator import Admin

admin = Admin('admin', 'X', '20', 'NY',['can add post','can delete post','can ban user'])
admin.privileges.show_privileges()