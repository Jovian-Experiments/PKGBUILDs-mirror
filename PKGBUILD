pkgname=steamos-devkit-service
pkgver=0.20220328.0
pkgrel=1
arch=('any')
url="https://gitlab.steamos.cloud/devkit/steamos-devkit-service"
license=('LGPL-2.1+')
source=(
    git+https://gitlab.steamos.cloud/devkit/steamos-devkit-service.git
    steamos-devkit-service.service
)
sha512sums=(
    SKIP
    SKIP
)
makedepends=('git' 'avahi' 'dbus-python' 'systemd')

package() {
    depends=('avahi' 'dbus-python' 'systemd')
    pkgdesc="SteamOS Devkit Service"
    install=steamos-devkit-service.install

    cd "${pkgname}"

    mkdir -p "${pkgdir}"/usr/lib/systemd/system
    cp "${srcdir}"/steamos-devkit-service.service "${pkgdir}"/usr/lib/systemd/system/

    mkdir -p "${pkgdir}"/usr/share/steamos-devkit
    cp -r "${srcdir}"/${pkgname}/hooks "${pkgdir}"/usr/share/steamos-devkit
    cp "${srcdir}"/${pkgname}/src/steamos-devkit-service.py "${pkgdir}"/usr/share/steamos-devkit
}
