#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-metadat
Version  : 1.2.0
Release  : 11
URL      : https://cran.r-project.org/src/contrib/metadat_1.2-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/metadat_1.2-0.tar.gz
Summary  : Meta-Analysis Datasets
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mathjaxr
BuildRequires : R-mathjaxr
BuildRequires : buildreq-R

%description
metadat: Meta-Analysis Datasets for R
=====================================
[![License: GPL (>=2)](https://img.shields.io/badge/license-GPL-blue)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![R build status](https://github.com/wviechtb/metadat/workflows/R-CMD-check/badge.svg)](https://github.com/wviechtb/metadat/actions)
[![CRAN Version](https://www.r-pkg.org/badges/version/metadat)](https://cran.r-project.org/package=metadat)
[![devel Version](https://img.shields.io/badge/devel-1.3--0-brightgreen.svg)](https://github.com/wviechtb/metadat)
[![Downloads](https://cranlogs.r-pkg.org/badges/grand-total/metadat)](https://cran.r-project.org/package=metadat)

%prep
%setup -q -c -n metadat
cd %{_builddir}/metadat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650585241

%install
export SOURCE_DATE_EPOCH=1650585241
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library metadat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library metadat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library metadat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc metadat || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/metadat/DESCRIPTION
/usr/lib64/R/library/metadat/INDEX
/usr/lib64/R/library/metadat/Meta/Rd.rds
/usr/lib64/R/library/metadat/Meta/data.rds
/usr/lib64/R/library/metadat/Meta/features.rds
/usr/lib64/R/library/metadat/Meta/hsearch.rds
/usr/lib64/R/library/metadat/Meta/links.rds
/usr/lib64/R/library/metadat/Meta/nsInfo.rds
/usr/lib64/R/library/metadat/Meta/package.rds
/usr/lib64/R/library/metadat/NAMESPACE
/usr/lib64/R/library/metadat/NEWS.md
/usr/lib64/R/library/metadat/R/metadat
/usr/lib64/R/library/metadat/R/metadat.rdb
/usr/lib64/R/library/metadat/R/metadat.rdx
/usr/lib64/R/library/metadat/data/Rdata.rdb
/usr/lib64/R/library/metadat/data/Rdata.rds
/usr/lib64/R/library/metadat/data/Rdata.rdx
/usr/lib64/R/library/metadat/help.rdata
/usr/lib64/R/library/metadat/help/AnIndex
/usr/lib64/R/library/metadat/help/aliases.rds
/usr/lib64/R/library/metadat/help/metadat.rdb
/usr/lib64/R/library/metadat/help/metadat.rdx
/usr/lib64/R/library/metadat/help/paths.rds
/usr/lib64/R/library/metadat/html/00Index.html
/usr/lib64/R/library/metadat/html/R.css
/usr/lib64/R/library/metadat/tests/testthat.R
/usr/lib64/R/library/metadat/tests/testthat/test_dat.aloe2013.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.anand1999.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.assink2016.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.axfors2021.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.bakdash2021.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.baker2009.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.bangertdrowns2004.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.baskerville2012.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.bcg.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.begg1989.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.berkey1998.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.besson2016.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.bonett2010.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.bornmann2007.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.bourassa1996.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.cannon2006.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.cohen1981.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.colditz1994.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.collins1985a.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.collins1985b.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.craft2003.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.crede2010.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.curtis1998.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.dagostino1998.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.damico2009.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.debruin2009.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.dogliotti2014.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.dong2013.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.dorn2007.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.egger2001.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.fine1993.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.franchini2012.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.frank2008.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.gibson2002.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.graves2010.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.gurusamy2011.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.hackshaw1998.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.hahn2001.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.hannum2020.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.hart1999.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.hartmannboyce2018.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.hasselblad1998.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.hine1989.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.ishak2007.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.kalaian1996.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.kearon1998.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.knapp2017.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.konstantopoulos2011.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.landenberger2005.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.laopaiboon2015.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.lau1992.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.lee2004.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.lehmann2018.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.li2007.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.lim2014.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.linde2005.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.linde2015.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.linde2016.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.lopez2019.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.maire2019.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.mccurdy2020.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.mcdaniel1994.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.michael2013.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.molloy2014.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.moura2021.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.nakagawa2007.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.nielweise2007.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.nielweise2008.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.normand1999.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.obrien2003.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.pagliaro1992.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.pignon2000.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.pritz1997.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.raudenbush1985.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.riley2003.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.senn2013.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.stowe2010.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.tannersmith2016.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.vanhowe1999.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.viechtbauer2021.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.white2020.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.woods2010.r
/usr/lib64/R/library/metadat/tests/testthat/test_dat.yusuf1985.r
