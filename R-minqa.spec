#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-minqa
Version  : 1.2.4
Release  : 14
URL      : http://cran.r-project.org/src/contrib/minqa_1.2.4.tar.gz
Source0  : http://cran.r-project.org/src/contrib/minqa_1.2.4.tar.gz
Summary  : Derivative-free optimization algorithms by quadratic
Group    : Development/Tools
License  : GPL-2.0
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n minqa

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library minqa
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library minqa


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/minqa/DESCRIPTION
/usr/lib64/R/library/minqa/INDEX
/usr/lib64/R/library/minqa/Meta/Rd.rds
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
/usr/lib64/R/library/minqa/libs/minqa.so
/usr/lib64/R/library/minqa/libs/symbols.rds
