import datetime
import sys

def get_lines():
    for line in sys.stdin:
        if not line.strip():
            continue
        yield line

def divide_line(line):
    return line.split("\t")

# Data Type	Count	Unique Values	Missing Values
#--- 0. ts	float64	2048442	668595	0
#--- 1. uid	object	2048442	479204	0
#--- 2. id.orig_h	object	2048442	71	0
#--- 3. id.orig_p	int64	2048442	37686	0
#--- 4. id.resp_h	object	2048442	88	0
#--- 5. id.resp_p	int64	2048442	8	0
# 6. trans_depth	int64	2048442	1207	0
#--- 7. method	object	2047566	143	876
#--- 8. host	object	2042003	315	6439
#--- 9. uri	object	2047566	1591739	876
# 10. referrer	object	382520	2485	1665922
# 11. user_agent	object	1977097	6560	71345
# 12. request_ body_len	int64	2048442	707	0
# 13. response_ body_len	int64	2048442	3839	0
# 14. status_code	float64	2011424	24	37018
# 15. status_msg	object	2011424	38	37018
# 16. info_code	float64	2	1	2048440
# 17. info_msg	object	2	1	2048440
# 18. filename	float64	0	0	2048442
# 19. tags	object	2048442	2	0
# 20. username	object	7146	120	2041296
# 21. password	float64	0	0	2048442
# 22. proxied	object	1154	183	2047288
# 23. orig_fuids	object	133222	133222	1915220
# 24. orig_mime_types	object	133222	18	1915220
# 25. resp_fuids	object	705213	701396	1343229
# 26. resp_mime_types	object	705213	29	1343229

def create_tuple(line):
    fields = divide_line(line)

    ts = datetime.datetime.fromtimestamp(float(fields[0]))
    uid = fields[1]
    id_orig_h = fields[2]
    id_orig_p = int(fields[3])
    id_resp_h = fields[4]
    id_resp_p = int(fields[5])
    method = fields[7]
    host = fields[8]
    uri = fields[9]
    return ts, uid, id_orig_h, id_orig_p, id_resp_h, id_resp_p, method, host, uri

def read_log():
    tuples = []
    for line in get_lines():
        tuples.append(create_tuple(line))
    return tuples