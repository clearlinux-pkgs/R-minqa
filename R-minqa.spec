#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-minqa
Version  : 1.2.4
Release  : 36
URL      : http://cran.r-project.org/src/contrib/minqa_1.2.4.tar.gz
Source0  : http://cran.r-project.org/src/contrib/minqa_1.2.4.tar.gz
Summary  : Derivative-free optimization algorithms by quadratic
Group    : Development/Tools
License  : GPL-2.0
Requires: R-minqa-lib
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers

%description
based on an interface to Fortran implementations by M. J. D.
        Powell.

%package lib
Summary: lib components for the R-minqa package.
Group: Libraries

%description lib
lib components for the R-minqa package.


%prep
%setup -q -c -n minqa

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502409747

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502409747
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library minqa
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library minqa
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library minqa
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/minqa/DESCRIPTION
/usr/lib64/R/library/minqa/INDEX
/usr/lib64/R/library/minqa/Meta/Rd.rds
/usr/lib64/R/library/minqa/Meta/features.rds
/usr/lib64/R/library/minqa/Meta/hsearch.rds
/usr/lib64/R/library/minqa/Meta/links.rds
/usr/lib64/R/library/minqa/Meta/nsInfo.rds
/usr/lib64/R/library/minqa/Meta/package.rds
/usr/lib64/R/library/minqa/NAMESPACE
/usr/lib64/R/library/minqa/R/minqa
/usr/lib64/R/library/minqa/R/minqa.rdb
/usr/lib64/R/library/minqa/R/minqa.rdx
/usr/lib64/R/library/minqa/help/AnIndex
/usr/lib64/R/library/minqa/help/aliases.rds
/usr/lib64/R/library/minqa/help/minqa.rdb
/usr/lib64/R/library/minqa/help/minqa.rdx
/usr/lib64/R/library/minqa/help/paths.rds
/usr/lib64/R/library/minqa/html/00Index.html
/usr/lib64/R/library/minqa/html/R.css
/usr/lib64/R/library/minqa/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/minqa/libs/minqa.so
/usr/lib64/R/library/minqa/libs/minqa.so.avx2
