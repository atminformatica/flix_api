from rest_framework import permissions

#lembrando pra funcionar tem que ir no admin e no usuario aplicar a 
#permissao poder visualizar e add model Genre
class GenrePermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','OPTIONS','HEAD']:
            return request.user.has_perm('genres.view_genre')
                                #significa permissao de view do model Genre no app genres
        if request.method =='POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATCH','put']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method =='DELETE':
            return request.user.has_perm('genres.destroy_genre')
        
        return False