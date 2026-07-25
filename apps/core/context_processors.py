def roles_uml(request):
    if not getattr(request, 'user', None) or not request.user.is_authenticated:
        return {}
    roles = set(request.user.roles_associes.values_list('role__libelle', flat=True))
    return {
        'user_roles': roles,
        'is_chef': 'Chef de Filière' in roles,
        'is_enseignant': 'Enseignant' in roles,
        'is_etudiant': 'Étudiant' in roles,
        'is_sga': 'SG-A' in roles,
    }
