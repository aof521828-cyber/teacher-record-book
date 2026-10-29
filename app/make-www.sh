#!/bin/sh
set -e
rm -rf www && mkdir -p www/lib
cp node_modules/exceljs/dist/exceljs.min.js www/lib/
cp node_modules/html2pdf.js/dist/html2pdf.bundle.min.js www/lib/
cp node_modules/@supabase/supabase-js/dist/umd/supabase.js www/lib/supabase.min.js
sed -e 's#https://cdnjs.cloudflare.com/ajax/libs/exceljs/4.4.0/exceljs.min.js#lib/exceljs.min.js#' \
    -e 's#https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js#lib/html2pdf.bundle.min.js#' \
    -e 's#https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js#lib/supabase.min.js#' \
    "$1" > www/index.html
grep -c 'src="lib/' www/index.html
