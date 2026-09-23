import json
d = json.load(open("webapp/data.json", encoding="utf-8"))
lines = []
lines.append("standings top5: " + str([(s["rank"], s["abbr"], s["record"]) for s in d["standings"][:5]]))
tb = d["teams"]["TB"]
lines.append("TB rank=%s roster=%s" % (tb["rank"], tb["rosterCount"]))
lines.append("TB QBs: " + str([(p["name"], p["impact"], p["jersey"]) for p in tb["groups"]["QB"][:3]]))
wr = tb["groups"]["WR"]
if wr:
    lines.append("TB WR[0]: " + json.dumps(wr[0], ensure_ascii=False))
open("jsoncheck.txt", "w", encoding="utf-8").write("\n".join(lines))
print("done")
