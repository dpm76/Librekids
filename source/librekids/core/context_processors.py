from librekids.settings import BASE_VERSION, TARGET_VERSION

def version(request):
    '''
    Provides version info to templates
    '''
    
    version = BASE_VERSION
    isDevVersion = BASE_VERSION != TARGET_VERSION
    
    return {"version": BASE_VERSION, "is_dev": isDevVersion}
