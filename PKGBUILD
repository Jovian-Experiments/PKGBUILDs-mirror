pkgname=steamos-devkit-service
pkgver=0.20220303.0
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
makedepends=('git' 'meson' 'json-glib' 'libsoup' 'avahi' 'systemd')

build() {
    cd "${pkgname}"
    meson --prefix=/usr --buildtype=plain src build
    meson compile -C build
}

package() {
    depends=('avahi' 'systemd')
    pkgdesc="SteamOS Devkit Service"
    install=steamos-devkit-service.install

    cd "${pkgname}"
    meson install -C build --destdir "$pkgdir"

    mkdir -p "${pkgdir}"/usr/lib/systemd/system
    cp "${srcdir}"/steamos-devkit-service.service "${pkgdir}"/usr/lib/systemd/system/

    mkdir -p "${pkgdir}"/usr/share/steamos-devkit
    cp -r "${srcdir}"/${pkgname}/hooks "${pkgdir}"/usr/share/steamos-devkit
}
