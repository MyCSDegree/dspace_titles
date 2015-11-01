DSPACE_BASE="10.1.32.27/"
NPROC=0

while read line; do
  url=`echo $line | tr -s "|" | cut -d '|' -f 4`
  echo $url
  wget --quiet --no-clobber --force-directories ${DSPACE_BASE}${url} &
  NPROC=$(($NPROC+1))
  if [ "$NPROC" -ge 64 ]; then
    wait
    NPROC=0
  fi
done < records.txt 
