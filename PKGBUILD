pkgname=steamos-devkit-service
pkgver=0.20220401.0
pkgrel=4
arch=('any')
url="https://gitlab.steamos.cloud/devkit/steamos-devkit-service"
license=('LGPL-2.1+')
_commit=3b924e16bea6009d464d497fae378c637407c4cf # tags/v0.20220401.0
source=(
    git+https://gitlab.steamos.cloud/devkit/steamos-devkit-service.git#commit=$_commit
    steamos-devkit-service.service
    devkit-service-on-os-update
    devkit-service-os-update.service
)
sha512sums=(
    SKIP
    a563dbb7452859d2632c6291eebf12547f484fcb1db4fe14044d3aea06c1c0e53c92dd9c5082ef91833af8158b9cde97e6f2fa271df45ed63b70bf95987385cd
    f2b44b4ee95740c7b5a49df88daa61226865397e7f8afaf7cfa4565425cf400ed2764c0bc8842bda88fad4186047d1b22ecac70ed5d301994ebd2a58c9ea3283
    ad3443d62396dfbf8204e6575cccfab79b5d7090f096ffbff80fa534e27012c39c3a26cfd38b335b438be9c9f2ea3c3d185f5c15ebb2f509adfd7850a236ab0c
)
makedepends=('git' 'avahi' 'dbus-python' 'systemd')

package() {
    depends=('avahi' 'dbus-python' 'systemd')
    pkgdesc="SteamOS Devkit Service"
    install=devkit-service-os-update.install

    cd "${pkgname}"

    mkdir -p "${pkgdir}"/usr/lib/systemd/system
    cp "${srcdir}"/steamos-devkit-service.service "${pkgdir}"/usr/lib/systemd/system/

    mkdir -p "${pkgdir}"/usr/bin
    cp "${srcdir}"/devkit-service-on-os-update "${pkgdir}"/usr/bin/
    cp "${srcdir}"/devkit-service-os-update.service "${pkgdir}"/usr/lib/systemd/system/

    mkdir -p "${pkgdir}"/usr/share/steamos-devkit
    cp -r "${srcdir}"/${pkgname}/hooks "${pkgdir}"/usr/share/steamos-devkit
    cp "${srcdir}"/${pkgname}/src/steamos-devkit-service.py "${pkgdir}"/usr/share/steamos-devkit
}
