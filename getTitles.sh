DSPACE_BASE="10.1.32.27/dspace/"
BROWSE_URL="browse-date"

mkdir -p PRE_DATA
rm -rf PRE_DATA/*


COUNT=1

function getURL() {
  DSPACE_URL=${DSPACE_BASE}${BROWSE_URL}
  COUNT_T="$(printf "%04d" ${COUNT})"
  wget -O PRE_DATA/${COUNT_T}.html ${DSPACE_URL}
  if grep -q 'browse-date?top=[0-9]\+%2F[0-9]\+' PRE_DATA/${COUNT_T}.html; then
    BROWSE_URL=`grep -o -e 'browse-date?top=[0-9]\+%2F[0-9]\+' PRE_DATA/${COUNT_T}.html | head -1`
    let COUNT=COUNT+1
    getURL
  else
    echo "done"
  fi
}

#init call
getURL
