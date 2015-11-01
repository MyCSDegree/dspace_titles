DSPACE_BASE="10.1.32.27/"
FILES=${DSPACE_BASE}dspace/handle/123456789/*

NPROC=0

for f in $FILES
do
  python ./004-getInfo.py $f &
  NPROC=$(($NPROC+1))
  if [ "$NPROC" -ge 64 ]; then
    wait
    NPROC=0
  fi
done
