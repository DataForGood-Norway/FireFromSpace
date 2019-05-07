# search the area you want to inspect on https://scihub.copernicus.eu/dhus/#/home
# apply filter on sentinel2,
# cloud coverage: [0 TO 20]
# product type: either nothing or 'S2MSI1C'
# Download images

for x in `ls *.jp2`; do echo "opj_decompress -i $x -o `basename $x .jp2`.png"; done | sh
