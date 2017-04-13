%{?_javapackages_macros:%_javapackages_macros}

Name:           sonar-plugins-parent
Version:        16
Release:        5%{?dist}
Summary:        Sonar Plugins Parent POM
Group:          Development/Java
License:        LGPLv3+
URL:            http://www.sonarqube.org
# svn export https://svn.codehaus.org/sonar-plugins/tags/parent-16/ sonar-plugins-parent-16
# tar cjf sonar-plugins-parent-16.tar.bz2 sonar-plugins-parent-16/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.codehaus.sonar:sonar-packaging-maven-plugin)

BuildArch:      noarch

%description
Sonar Plugins Parent POM.

%prep
%setup -q

%pom_xpath_remove pom:build/pom:extensions
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%mvn_file ':{*}' @1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Michael Simacek <msimacek@redhat.com> - 16-3
- Remove enforcer-plugin

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Michael Simacek <msimacek@redhat.com> - 16-1
- Initial version
