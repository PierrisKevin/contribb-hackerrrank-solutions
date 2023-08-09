import mysql.connector
import jaro
import pandas as pd


# def replace_none_charactere(text):
#     regex = r"[^\w\s]"
#     cleaned_text = re.sub(regex, " ", text)

#     return cleaned_text
conn = mysql.connector.connect(
    host="41.207.44.69",
    user="narisoa", 
    password="datascience10datamanager11", 
    database="prod_ing" 
)

cursor = conn.cursor()

query = """

    SELECT distinct nom_region,nom_district, nom_commune, f.nom_fokontany, m.num_menage,r.num_iteration as iteration_dans_menage,r.id_reponse as ID_DB,r.INDIV_C as code_individu, if(r.m7 in (56,217),"Chef menage lui meme",if(r.m7 in (57,218),"Conjoint",if(r.m7 in (58,219),"Enfant",if(r.m7 in (59,220),"parent du Chef menage","Autre")))) as relation_avec_cm,
    r.m1a as nm_individu, r.m1b as prenoms_individus, if(r.m3=49,'F',if(r.m3=48,'H','non definit')) as sexe_individus,
    r.m4 as age_individus,r.m6a as cin, if(r.m15=1,"OUI","NON") as scolarise, if(r.CQSuivreFE=1,"OUI","NON") as suivi_Femme_enceinte, if(r.m12=1,"OUI",if(r.m12=0,"NON","")) as femme_enceinte,
    if(r.CQSuivreAEC=1,"OUI","NON") as suivi_AEC, if(CQSuivreAUE=1,"OUI","NON")  as suivi_AUE, MOIS_DPA
    FROM registre_activite ra 
    inner join activite act on act.id_activite=ra.id_activite
    inner join 
    menage_valider v on v.id_menage_valider=ra.id_menage_valider
    inner join menage_a_enqueter q on q.id_menage_enquete=v.id_menage_enquete 
    inner join menage m on m.id_menage=q.id_menage 
    inner join fokontany f on f.id_fokontany=m.id_fokontany 
    inner join commune c on c.id_commune=f.id_commune 
    inner join district d on d.id_district=c.id_district
    inner join region reg on reg.id_region=d.id_region 
    inner join direction dir on dir.id_direction=reg.id_direction
    inner join reponse_53 r on r.id_menage=m.id_menage 
    where act.id_type_activite=44

"""
cursor.execute(query)

results = cursor.fetchall()
result_tab = list(results)
doublon_list = []

# print(results)
for i in results:
    personne = str(i[9])+" "+str(i[10])
    personne_cin = str(i[13])
    personne_age = str(i[12])
    result = []
    for j in results:
        name_to_test = str(j[9])+" "+str(j[10])
        cin_to_test = str(j[13])
        percentages = round(jaro.jaro_winkler_metric(u""+name_to_test, u""+personne), 2)
        if percentages>0.9:
            if len(personne_cin)>0:
                if len(str(j[13]))>0:
                    if str(j[13])==personne_cin:
                        result.append("-(Par ressemblance de Numero CIN) "+name_to_test+" a un resemblance de nom a : "+str(percentages*100)+" avec l'identifiant : " + str(j[7]) + " CIN : "+ cin_to_test)
                else:
                    if str(j[12])==personne_age:
                        result.append("-(Par ressemblance d'Age) "+name_to_test+" a un resemblance de nom a : "+str(percentages*100)+" avec l'identifiant : " + str(j[7]))
            else:
                if str(j[12])==personne_age:
                        result.append("-(Par ressemblance d'Age) "+name_to_test+" a un resemblance de nom a : "+str(percentages*100)+" avec l'identifiant : " + str(j[7]))
        else:
            if cin_to_test==personne_cin and personne_cin!="" and personne_cin and personne_cin!="None" and personne_cin!="0":
                print("cin du personne"+ personne_cin)
                result.append("-(Par ressemblance de Numero CIN mais nom different) "+name_to_test+" avec l'identifiant : " + str(j[7]) +" CIN : "+ str(cin_to_test)+"***")


    if len(result)>1 and result not in doublon_list:
        doublon_list.append(["*Pour le nom de "+personne+" avec le CIN "+personne_cin+" : "]+result)

# print("\n".join(doublon_list))

cursor.close()
conn.close()

noveau_donne = [reponse for liste in doublon_list for reponse in liste]
nombre = 2
limit = 0
if len(noveau_donne)>300:
    while limit<len(noveau_donne):
        df = pd.DataFrame(noveau_donne[limit:limit+500], columns=["Information des paiement"])
        path = "./hight_comp/doublon_list"+ str(nombre) +".xlsx"
        df.to_excel(path, index=False)
        limit+=500
        nombre+=1
else:
    df = pd.DataFrame(noveau_donne[limit:limit+300], columns=["Information des paiement"])
    path = "./hight_comp/doublon_list"+ str(nombre) +".xlsx"
    df.to_excel(path, index=False)
    limit+=500
    nombre+=1

print("Enregistrement des fichiers reussi...")