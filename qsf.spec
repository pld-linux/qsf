#
# Conditional build:
%bcond_without	gdbm		# build without gdbm backend
%bcond_with	mysql		# build with MySQL backend
%bcond_with	sqlite		# build with SQLite2 backend
#
Summary:	Quick spam filter
Summary(pl):	Szybki filtr antyspamowy
Name:		qsf
Version:	1.2.6
Release:	1
License:	Artistic
Group:		Applications
Source0:	http://dl.sourceforge.net/qsf/%{name}-%{version}.tar.bz2
# Source0-md5:	45926441d247f72778a01092f6a83743
URL:		http://www.ivarch.com/programs/qsf.shtml
%{?with_gdbm:BuildRequires:	gdbm-devel}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quick Spam Filter (qsf) is a small, fast spam filter that works by
learning to recognise the words that are more likely to appear in spam
than non-spam. It is intended to be used in a procmail recipe to mark
email as being possible spam.

%description -l pl
Quick Spam Filter (qsf) to ma³y, szybki filtr antyspamowy dzia³aj±cy
poprzez uczenie siê rozpoznawania s³ów, które czê¶ciej wystêpuj± w
spamie ni¿ nie-spamie. Jest przeznaczony do u¿ywania w regu³ce
procmaila do oznaczania poczty bêd±cej prawdopodobnie spamem.

%prep
%setup -q

%build
%configure \
	%{!?with_gdbm:--without-gdbm} \
	%{!?with_mysql:--without-mysql} \
	%{!?with_sqlite:--without-sqlite}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/{NEWS,TODO,postfix-howto}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
