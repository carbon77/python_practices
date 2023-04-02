import re


def main(s):
    s = s.replace('\n', ' ')
    r1 = re.compile(r'<section>([^<>]+)</section>')
    r2 = re.compile(r' *loc *([0-9a-zA-Z_]+) +is *#\((.*)\)')
    r3 = re.compile(r'\"([^\"]*)\"')

    section_bodies = r1.findall(s)
    result = {}

    for sb in section_bodies:
        key, values_str = r2.findall(sb)[0]
        values = r3.findall(values_str)
        result[key] = values

    return result


print(main('''
<< <section> loc orri_939 is#("erveon" ."matire_464". "esri" ).
</section>.<section> loc rera is #( "orreed_181"."oresce_766".
"cedige_574" ."diised_621"). </section>. <section> loc maondi_369 is
#( "inla_588" . "maalexe_539" ."beri_186" ). </section>.<section>loc
ceriqu is #( "zaarce" . "enza" . "zage" . "inzaza" ).</section>.>>
'''))

