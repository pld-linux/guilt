Summary:	Guilt (Git quilt) - queue-like functionality for git
Summary(pl.UTF-8):	Guilt (Git quilt) - funkcjonalność kolejek dla git
Name:		guilt
Version:	0.29
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.kernel.org/pub/linux/kernel/people/jsipek/guilt/%{name}-%{version}.tar.gz
# Source0-md5:	60bec919963d7cb7d299aa217747e722
Patch0:		%{name}-DESTDIR.patch
URL:		http://git.kernel.org/?p=linux/kernel/git/jsipek/guilt.git
BuildRequires:	asciidoc
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guilt (Git Quilt) is a series of bash scripts which add a Mercurial
queues-like functionality and interface to git.

%description -l pl.UTF-8
Guilt (Git Quilt) to zestaw skryptów powłoki dodających do git podobną
do Mercurial funkcjonalność obsługi kolejek.

%prep
%setup -q
%patch0 -p1
mkdir Documentation/{html,txt}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-doc \
	PREFIX=%{_prefix} \
	mandir=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

cp Documentation/*.html Documentation/html
cp Documentation/*.txt  Documentation/txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation/html Documentation/txt Documentation/{Contributing,Features,HOWTO,Requirements}
%{_mandir}/man1/*
%{_mandir}/man7/*
%attr(755,root,root) %{_bindir}/*
