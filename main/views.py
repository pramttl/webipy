from django.shortcuts import render
from django.http import HttpResponse

import os, sys

import inspect
from inspect import getmembers, isfunction
import myfunctions
import json

functions_list = [o for o in getmembers(myfunctions) if isfunction(o[1])]

function_map = {}

# Mapping between function name: function_object, function_arugments
for element in functions_list:
    fname = element[0]
    fobj = element[1]
    #fargs = inspect.getargspec(fobj)[0]
    function_map[fname] = fobj


def master_view(request, fname):
    fname = str(fname)
    get_query_dict = request.GET
    args_dict = {}
    for k,v in get_query_dict.items():
        args_dict[k] = v[0]

    #print args_dict
    func = function_map[fname]
    output = func(**args_dict)

    return HttpResponse(json.dumps(output), content_type='application/json')
