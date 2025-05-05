pkgname=steamos-devkit-service
pkgdesc="SteamOS Devkit Service"
pkgver=0.20250428.0
pkgrel=3
arch=('any')
url="https://gitlab.steamos.cloud/devkit/steamos-devkit-service"
license=('LGPL-2.1+')
source=(
    git+https://gitlab.steamos.cloud/devkit/steamos-devkit-service.git#tag=v"$pkgver"
    steamos-devkit-service.service
)
sha512sums=('2bb1279b97b4df20f2f8e320b8038eaa248b97f5aa35180420ec5b0d9639e19c4705b1d821e67ff4ea576000d65dbc8694c5d798bda02c90f7fac7b8bd5096d9'
            'a563dbb7452859d2632c6291eebf12547f484fcb1db4fe14044d3aea06c1c0e53c92dd9c5082ef91833af8158b9cde97e6f2fa271df45ed63b70bf95987385cd')
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
