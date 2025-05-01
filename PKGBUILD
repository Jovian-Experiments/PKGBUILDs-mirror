pkgname=steamos-devkit-service
pkgdesc="SteamOS Devkit Service"
pkgver=0.20250428.0
pkgrel=2
arch=('any')
url="https://gitlab.steamos.cloud/devkit/steamos-devkit-service"
license=('LGPL-2.1+')
_commit=55b3a15011163b4ab861aa84e05ae3672ab1a75c
source=(
    git+https://gitlab.steamos.cloud/devkit/steamos-devkit-service.git#commit=$_commit
    steamos-devkit-service.service
)
sha512sums=(
    SKIP
    a563dbb7452859d2632c6291eebf12547f484fcb1db4fe14044d3aea06c1c0e53c92dd9c5082ef91833af8158b9cde97e6f2fa271df45ed63b70bf95987385cd
)
makedepends=('git' 'avahi' 'dbus-python' 'systemd')

package() {
    depends=('avahi' 'dbus-python' 'systemd')
    pkgdesc="SteamOS Devkit Service"

    cd "${pkgname}"

    mkdir -p "${pkgdir}"/usr/lib/systemd/system
    cp "${srcdir}"/steamos-devkit-service.service "${pkgdir}"/usr/lib/systemd/system/

    mkdir -p "${pkgdir}"/usr/share/steamos-devkit
    cp -r "${srcdir}"/${pkgname}/hooks "${pkgdir}"/usr/share/steamos-devkit
    cp "${srcdir}"/${pkgname}/src/steamos-devkit-service.py "${pkgdir}"/usr/share/steamos-devkit
}
