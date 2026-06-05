import time
def response_length(t): return len(t.split())
def similarity_score(a,b):
 x={w.lower().strip('.,!?;') for w in a.split()}; y={w.lower().strip('.,!?;') for w in b.split()}; return 1.0 if not x and not y else round(len(x&y)/max(len(x|y),1),4)
def adherence_score(prompt,response):
 if not response.strip(): return 0.0
 keys=[w.lower().strip('.,!?') for w in prompt.split() if len(w)>4]
 return 1.0 if not keys else round(min(1.0,sum(1 for w in keys if w in response.lower())/max(len(keys),1)+0.25),4)
def timed_generate(gen,prompt):
 s=time.perf_counter(); out=gen(prompt); return out,round(time.perf_counter()-s,6)
