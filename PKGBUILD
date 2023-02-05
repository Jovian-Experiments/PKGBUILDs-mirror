# Maintainer: Joshua Ashton <joshua@froggi.es>
pkgname=steam_notif_daemon
pkgver=v1.0.1
pkgrel=1
license=('MIT')
pkgdesc='Simple XDG D-Bus Notification wrapper'
makedepends=("meson" "systemd" "git")
depends=(
    "systemd-libs"
    "curl"
)
arch=("x86_64")
url='https://gitlab.steamos.cloud/jupiter/steam_notif_daemon'
source=(
    "${pkgname%-*}::git+ssh://git@gitlab.steamos.cloud/jupiter/steam_notif_daemon.git#tag=$pkgver"
)
sha512sums=('SKIP')

build() {
    cd "$pkgname"
    arch-meson -Dsd-bus-provider=libsystemd build
    ninja -C build
}

package() {
    cd "$pkgname"
    DESTDIR="$pkgdir/" ninja -C build install
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/"${pkgname%-*}"/LICENSE
}
