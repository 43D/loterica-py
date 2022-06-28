import imp
import re
from venv import create
import requests
import datetime
from django.shortcuts import render
from django.views import View
from django.http import Http404, JsonResponse

from app import views

from .models import *


class ToDicionay():
    def MSConcursoToDicionary(MSConcursos, value):
        data = {}
        data["concurso"] = MSConcursos.id_concurso
        data["data"] = MSConcursos.data
        data["valores"] = str(value.v1) + "-" + str(value.v2) + "-" + str(
            value.v3) + "-" + str(value.v4) + "-" + str(value.v5) + "-" + str(value.v6)
        return data

    def MSValoresToDicionary(MSValores, MSConcursos):
        data = {}
        data["concurso"] = MSValores.id_concurso.id_concurso
        data["data"] = MSConcursos.data
        numeros = {}
        numeros["numero_1"] = MSValores.v1
        numeros["numero_2"] = MSValores.v2
        numeros["numero_3"] = MSValores.v3
        numeros["numero_4"] = MSValores.v4
        numeros["numero_5"] = MSValores.v5
        numeros["numero_6"] = MSValores.v6
        data["numeros"] = numeros
        return data

    def GenericConjutoToDicionarySummary(conjunto):
        conj = {}
        conj["id"] = conjunto.id
        conj["contador"] = conjunto.quantidade
        conj["media_frequencia"] = conjunto.media_frequencia
        return conj

    def GenericConjutoToDicionary(conjunto):
        conj = {}
        conj["id"] = conjunto.id
        conj["contador"] = conjunto.quantidade
        conj["media_frequencia"] = conjunto.media_frequencia

        val = {}
        for key in conjunto._meta.fields:
            if("v" in str(key).split(".")[-1]):
                j = getattr(conjunto, str(key).split(".")[-1])
                val[str(key).split(".")[-1]] = j
        conj["valores"] = val
        return conj

    def ConjutoToDicionarySummary(conjunto_concurso, op):
        option = {0: ToDicionay.GenericConjutoToDicionarySummary,
                  1: ToDicionay.GenericConjutoToDicionary}
        collection = {}
        for i in conjunto_concurso:
            j = option[op](i.value)
            collection[j["id"]] = j
        return collection

    def ConjutosToDicionary(concurso):
        data = {}

        option = {0: [single_Mega_sena_concurso, 'unico'],
                  1: [double_Mega_sena_concurso, 'duplo'],
                  2: [triple_Mega_sena_concurso, 'triplo'],
                  3: [quadruple_Mega_sena_concurso, 'quadruplo'],
                  4: [quintuple_Mega_sena_concurso, 'quintuplo'],
                  5: [sextuple_Mega_sena_concurso, 'sextuplo']}
        for i in option:
            try:
                data[option[i][1]] = ToDicionay.ConjutoToDicionarySummary(
                    option[i][0].objects.filter(concurso__id=concurso.id), 0)
            except:
                data[option[i][1]] = {}
        return data


class GetConjunto():
    def getConjunto(op):
        option = {0: single_Mega_sena_concurso,
                  1: double_Mega_sena_concurso,
                  2: triple_Mega_sena_concurso,
                  3: quadruple_Mega_sena_concurso,
                  4: quintuple_Mega_sena_concurso,
                  5: sextuple_Mega_sena_concurso}
        lista = option[op].objects.all()
        data = ToDicionay.ConjutoToDicionarySummary(lista, 1)
        return data

    def genOne(n):
        return n

    def genTwo(n):
        if(len(n) == 2):
            return ["-".join(n)]
        elif(len(n) > 2):
            nuns = []
            for z in range(0, len(n)-1):
                for y in range(z+1, len(n)):
                    nuns.append(n[z] + "-"+n[y])
            return nuns
        return ["0"]

    def genThree(n):
        if(len(n) == 3):
            return ["-".join(n)]
        elif(len(n) > 3):
            nuns = []
            for z in range(0, len(n)-2):
                for y in range(z+1, len(n)-1):
                    for x in range(y+1, len(n)):
                        nuns.append(n[z] + "-"+n[y]+"-"+n[x])
            return nuns
        return ["0"]

    def genFour(n):
        if(len(n) == 4):
            return ["-".join(n)]
        elif(len(n) > 4):
            nuns = []
            for z in range(0, len(n)-3):
                for y in range(z+1, len(n)-2):
                    for x in range(y+1, len(n)-1):
                        for w in range(x+1, len(n)):
                            nuns.append(n[z] + "-"+n[y]+"-"+n[x] + "-" + n[w])
            return nuns
        return ["0"]

    def genFive(n):
        if(len(n) == 5):
            return ["-".join(n)]
        elif(len(n) > 5):
            nuns = []
            for z in range(0, len(n)-4):
                for y in range(z+1, len(n)-3):
                    for x in range(y+1, len(n)-2):
                        for w in range(x+1, len(n)-1):
                            for t in range(w+1, len(n)):
                                nuns.append(n[z] + "-"+n[y]+"-" +
                                            n[x] + "-" + n[w] + "-" + n[t])
            return nuns
        return ["0"]

    def genSix(n):
        return ["-".join(n)]

    def getList(cj, object):
        data = []
        for id in cj:
            lista = object.objects.filter(value=id)
            if(lista):
                data.append(ToDicionay.ConjutoToDicionarySummary(lista, 1))
        return data

    def getOne(len, value):
        data = {}
        option = {0: [single_Mega_sena_concurso, GetConjunto.genOne],
                  1: [double_Mega_sena_concurso, GetConjunto.genTwo],
                  2: [triple_Mega_sena_concurso, GetConjunto.genThree],
                  3: [quadruple_Mega_sena_concurso, GetConjunto.genFour],
                  4: [quintuple_Mega_sena_concurso, GetConjunto.genFive],
                  5: [sextuple_Mega_sena_concurso, GetConjunto.genSix]}

        for op in range(len):
            cj = option[op][1](value)
            data[op] = GetConjunto.getList(cj, option[op][0])
        return data


class MakeConjunto():
    def makeUp(nuns, conjunto, i, op):
        option = {0: [single_value_mega_sena, single_Mega_sena_concurso],
                  1: [double_value_mega_sena, double_Mega_sena_concurso],
                  2: [triple_value_mega_sena, triple_Mega_sena_concurso],
                  3: [quadruple_value_mega_sena, quadruple_Mega_sena_concurso],
                  4: [quintuple_value_mega_sena, quintuple_Mega_sena_concurso],
                  5: [sextuple_value_mega_sena, sextuple_Mega_sena_concurso]}

        exist = option[op][0].objects.filter(id=i)
        if exist:
            exist.update(quantidade=exist[0].quantidade+1)
            m = exist[0].media_frequencia
            if m == 0:
                exist.update(
                    media_frequencia=exist[0].ultimo_concurso - conjunto.id_concurso.id)
            else:
                exist.update(media_frequencia=(
                    m+exist[0].ultimo_concurso - conjunto.id_concurso.id)/2)

        else:
            c1 = option[op][0](id=i, v1=nuns[0], quantidade=1, media_frequencia=0,
                               ultimo_concurso=conjunto.id_concurso.id, create_at=datetime.datetime.now().date().strftime("%Y-%m-%d"))
            match op:
                case 1:
                    c1.v2 = nuns[1]
                case 2:
                    c1.v2 = nuns[1]
                    c1.v3 = nuns[2]
                case 3:
                    c1.v2 = nuns[1]
                    c1.v3 = nuns[2]
                    c1.v4 = nuns[3]
                case 4:
                    c1.v2 = nuns[1]
                    c1.v3 = nuns[2]
                    c1.v4 = nuns[3]
                    c1.v5 = nuns[4]
                case 5:
                    c1.v2 = nuns[1]
                    c1.v3 = nuns[2]
                    c1.v4 = nuns[3]
                    c1.v5 = nuns[4]
                    c1.v6 = nuns[5]

            c1v = option[op][1](value=c1, concurso=conjunto.id_concurso)
            c1.save()
            c1v.save()

    def MakeOne(nuns, conjunto):
        for i in nuns:
            MakeConjunto.makeUp([i], conjunto, i, 0)

    def MakeTwo(nuns, conjunto):
        for z in range(0, 5):
            for y in range(z+1, 6):
                i = str(nuns[z]) + "-" + str(nuns[y])
                MakeConjunto.makeUp([nuns[z], nuns[y]], conjunto, i, 1)

    def MakeThree(nuns, conjunto):
        for z in range(0, 4):
            for y in range(z+1, 5):
                for x in range(y+1, 6):
                    i = str(nuns[z]) + "-" + str(nuns[y]) + "-" + str(nuns[x])
                    MakeConjunto.makeUp(
                        [nuns[z], nuns[y], nuns[x]], conjunto, i, 2)

    def MakeFour(nuns, conjunto):
        for z in range(0, 3):
            for y in range(z+1, 4):
                for x in range(y+1, 5):
                    for w in range(x+1, 6):
                        i = str(nuns[z]) + "-" + str(nuns[y]) + \
                            "-" + str(nuns[x]) + "-" + str(nuns[w])
                        MakeConjunto.makeUp(
                            [nuns[z], nuns[y], nuns[x], nuns[w]], conjunto, i, 3)

    def MakeFive(nuns, conjunto):
        for z in range(0, 2):
            for y in range(z+1, 3):
                for x in range(y+1, 4):
                    for w in range(x+1, 5):
                        for t in range(w+1, 6):
                            i = str(nuns[z]) + "-" + str(nuns[y]) + "-" + \
                                str(nuns[x]) + "-" + \
                                str(nuns[w]) + "-" + str(nuns[t])
                            MakeConjunto.makeUp(
                                [nuns[z], nuns[y], nuns[x], nuns[w], nuns[t]], conjunto, i, 4)

    def MakeSix(nuns, conjunto):
        i = str(nuns[0]) + "-" + str(nuns[1]) + "-" + str(nuns[2]) + \
            "-" + str(nuns[3]) + "-" + str(nuns[4]) + "-" + str(nuns[5])
        MakeConjunto.makeUp(
            [nuns[0], nuns[1], nuns[2], nuns[3], nuns[4], nuns[5]], conjunto, i, 5)

    def make(conjunto):
        nums = [conjunto.v1, conjunto.v2, conjunto.v3,
                conjunto.v4, conjunto.v5, conjunto.v6]
        modelos = (MakeConjunto.MakeOne(nums, conjunto))
        modelos = (MakeConjunto.MakeTwo(nums, conjunto))
        modelos = (MakeConjunto.MakeThree(nums, conjunto))
        modelos = (MakeConjunto.MakeFour(nums, conjunto))
        modelos = (MakeConjunto.MakeFive(nums, conjunto))
        modelos = (MakeConjunto.MakeSix(nums, conjunto))


class Util():
    def atualizar():
        r = requests.get(
            url='https://loterias-gutotech.herokuapp.com/api/mega-sena/')
        data = r.json()

        list_ids = Mega_sena_concurso.objects.values_list(
            "id_concurso", flat=True)

        numeros = []
        for x in data:
            if not (x['concurso'] in list_ids):
                numeros.append(x)

        for y in numeros:
            c = y['data'].split("/")
            a = Mega_sena_concurso(
                id_concurso=y['concurso'], data=c[2]+"-"+c[1]+"-"+c[0])
            a.save()
            b = Mega_sena_valores(v1=y['dezenas'][0], v2=y['dezenas'][1], v3=y['dezenas'][2],
                                  v4=y['dezenas'][3], v5=y['dezenas'][4], v6=y['dezenas'][5], id_concurso=a)
            b.save()

            MakeConjunto.make(b)
        return {"STATUS": "OK"}

    def consultar(nuns):
        conjuntos = []
        for x in sorted(nuns):
            if(x > 0 and x < 60):
                if (x < 10):
                    conjuntos.append("0" + str(x))
                else:
                    conjuntos.append(str(x))

        data = GetConjunto.getOne(len(conjuntos), conjuntos)
        return data


# Create your views here.


class ConcursoMSView(View):
    def get(self, request):
        try:
            MSConcursos = Mega_sena_concurso.objects.all()
            data = []
            for i in (MSConcursos):
                MSValores = i.mega_sena_valores
                data.append(ToDicionay.MSConcursoToDicionary(i, MSValores))
        except:
            raise Http404
        else:
            return JsonResponse(data, safe=False)


class ValoresMSView(View):
    def get(self, request, ms_id):
        try:
            MSConcursos = Mega_sena_concurso.objects.get(id_concurso=ms_id)
            MSValores = MSConcursos.mega_sena_valores
            data = ToDicionay.MSValoresToDicionary(MSValores, MSConcursos)
        except:
            raise Http404
        else:
            return JsonResponse(data, safe=False)


class ConcursoConjuntoView(View):
    def get(self, request, ms_id):
        try:
            concurso = Mega_sena_concurso.objects.get(id_concurso=ms_id)
            data = ToDicionay.ConjutosToDicionary(concurso)
        except:
            raise Http404
        else:
            return JsonResponse(data, safe=False)


class ConjuntoView(View):
    def get(self, request):
        data = {}
        op = ["unico", "duplo", "triplo", "quadruplo", "quintuplo", "sextuplo"]
        data["opcoes"] = op
        return JsonResponse(data, safe=False)


class ConjuntosView(View):
    def get(self, request, url):
        option = {"unico": 0, "duplo": 1, "triplo": 2,
                  "quadruplo": 3, "quintuplo": 4, "sextuplo": 5}
        try:
            data = {url: GetConjunto.getConjunto(option[url])}
        except:
            raise Http404
        else:
            return JsonResponse(data, safe=False)


class ConjuntosDetailView(View):
    def get(self, request, url,  c_id):
        option = {"unico": single_value_mega_sena,
                  "duplo": double_value_mega_sena,
                  "triplo": triple_value_mega_sena,
                  "quadruplo": quadruple_value_mega_sena,
                  "quintuplo": quintuple_value_mega_sena,
                  "sextuplo": sextuple_value_mega_sena}
        try:
            if re.findall("[0-9]{2,12}", str(c_id)):
                conjunto = option[url].objects.get(id=str(c_id))
                data = ToDicionay.GenericConjutoToDicionary(conjunto)
        except:
            raise Http404
        else:
            return JsonResponse(data, safe=False)


class MainView(View):
    def get(self, request):
        data = {}
        op = ["atualizar", "consultar", "concurso", "conjunto"]
        data["opcoes"] = op
        return JsonResponse(data, safe=False)


class UpdateView(View):
    def get(self, request):

        data = Util.atualizar()

        return JsonResponse(data, safe=False)


class ConsultarDetalhesView(View):
    def get(self, request):

        data = {}
        op = {"1": "/int/", "2": "/int/int/", "3": "/int/int/int/", "4": "/int/int/int/int/",
              "5": "/int/int/int/int/int/", "6": "/int/int/int/int/int/int/"}
        data["opcoes"] = op

        return JsonResponse(data, safe=False)


class ConsultarView(View):
    def get(self, request, v1=-1, v2=-1, v3=-1, v4=-1, v5=-1, v6=-1):
        nuns = [v1, v2, v3, v4, v5, v6]
        data = Util.consultar(nuns)
        return JsonResponse(data, safe=False)
