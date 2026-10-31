import pathlib,sys,subprocess,os,concurrent.futures,time,json,hashlib
base=pathlib.Path('/mnt/data/yau26_rounds12_audit_20260921');root=pathlib.Path((base/'root.txt').read_text())/'proofs'
scripts=sorted(root.glob('*.py')); start,end=map(int,sys.argv[1:3]);out=base/'rerun';out.mkdir(exist_ok=True)
worker='import resource,runpy,sys;resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,3*1024**3));resource.setrlimit(resource.RLIMIT_CPU,(30,32));runpy.run_path(sys.argv[1],run_name="__main__")'
env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONHASHSEED='0')
def run(p):
 t=time.monotonic()
 try:
  r=subprocess.run([sys.executable,'-I','-c',worker,str(p)],cwd=root,env=env,timeout=33,capture_output=True,text=True)
  status='passed' if r.returncode==0 else 'failed';msg=r.stdout+'\n'+r.stderr;code=r.returncode
 except subprocess.TimeoutExpired as e:status='timeout';msg=str(e);code=None
 rec=dict(script=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),status=status,returncode=code,seconds=round(time.monotonic()-t,2))
 (out/(p.stem+'.txt')).write_text(msg);(out/(p.stem+'.json')).write_text(json.dumps(rec,ensure_ascii=False,indent=2));return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 for rec in pool.map(run,scripts[start:end]):print(json.dumps(rec),flush=True)
print('Scripts in total',len(scripts))
