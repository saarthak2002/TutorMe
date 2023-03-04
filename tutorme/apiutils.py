import requests
import re

def get_data_for_class(subject, catalog_nbr):
    ret = []
    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&page=1'
    r = requests.get(url + '&subject=' + subject + '&catalog_nbr=' + catalog_nbr)
    parsed = r.json()
    for entry in parsed:
        instructor_name = entry['instructors'][0]
        class_entry = {'section':entry['class_section'], 'subject':entry['subject'], 'catalog':entry['catalog_nbr'],'class_name':entry['descr'], 'instructor':instructor_name['name']}
        ret.append(class_entry)
    return ret

def get_data_for_class_by_subject(subject):
    ret = []
    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&page=1'
    r = requests.get(url + '&subject=' + subject)
    parsed = r.json()
    for entry in parsed:
        instructor_name = entry['instructors'][0]
        class_entry = {'section':entry['class_section'], 'subject':entry['subject'], 'catalog':entry['catalog_nbr'],'class_name':entry['descr'], 'instructor':instructor_name['name']}
        ret.append(class_entry)
    return ret

def get_data_by_keyword(keyword):
    ret = []
    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&page=1'
    r = requests.get(url + '&keyword=' + keyword)
    parsed = r.json()
    for entry in parsed:
        instructor_name = entry['instructors'][0]
        class_entry = {'section':entry['class_section'], 'subject':entry['subject'], 'catalog':entry['catalog_nbr'],'class_name':entry['descr'], 'instructor':instructor_name['name']}
        ret.append(class_entry)
    return ret

def regex_pattern_matcher_class_catalog(text):
    pattern = "^[A-Z]{2,4}\s\d{4}$"

    if re.match(pattern, text):
        return True
    else:
        return False

def regex_pattern_matcher_class(text):
    pattern = "^[A-Z]{2,4}$"

    if re.match(pattern, text):
        return True
    else:
        return False
    
def search_matcher(text):
    if regex_pattern_matcher_class(text):
        return get_data_for_class_by_subject(text)
    
    elif regex_pattern_matcher_class_catalog(text):
        search_list = text.split(' ')
        return get_data_for_class(search_list[0], search_list[1])
    
    else:
        return get_data_by_keyword(text)
