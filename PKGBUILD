# Maintainer: Collabora Ltd <arnaud.rebillout@collabora.com>

pkgname=steamos-media-creation-git
pkgver=r115.dca5287
pkgrel=5
pkgdesc='SteamOS Media Creation'
arch=('x86_64')
url='http://repo.steampowered.com'
license=('LGPL2.1')
depends=('python-dbus' 'python-tzlocal' 'qt5-base'
  'python>=3.11'
  'python<3.12'
)
makedepends=('git')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
options=(!strip)
source=("${pkgname%-git}::git+https://gitlab.steamos.cloud/steam/${pkgname%-git}.git#commit=dca5287")
sha256sums=('SKIP')

pkgver() {
    cd "${pkgname%-git}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    cd "${pkgname%-git}"
}

build() {
    cd "${pkgname%-git}"

    qmake-qt5 PREFIX=/usr BINDIR=/usr/lib/steamos-media-creation LIBDIR=/usr/lib
    make
}

package() {
    cd "${pkgname%-git}"

    make INSTALL_ROOT="$pkgdir" install

    mkdir -p "$pkgdir/usr/lib/"
    install -Dm755 buildlinux/steamos-media-creation "$pkgdir/usr/bin/steamos-media-creation"
    install -Dm755 "$srcdir/${pkgname%-git}/installer.py" "$pkgdir/usr/lib/steamos-media-creation"
    cp -a "$srcdir/${pkgname%-git}/buildlinux/etcher-sdk/"* "$pkgdir/usr/lib/steamos-media-creation"
    install -Dm644 "$startdir/steamos-media-creation.png" "$pkgdir/usr/share/icons/512x512/apps/steamos-media-creation.png"
    install -Dm644 "$srcdir/${pkgname%-git}/support/steamos-media-creation.desktop" "$pkgdir/usr/share/applications/steamos-media-creation.desktop"
    install -Dm644 "$srcdir/${pkgname%-git}/support/com.valvesoftware.steamos-media-creation.policy" "$pkgdir/usr/share/polkit-1/actions/com.valvesoftware.steamos-media-creation.policy"
    install -Dm644 "$srcdir/${pkgname%-git}/support/com.valvesoftware.steamos-media-creation.rules" "$pkgdir/usr/share/polkit-1/rules.d/com.valvesoftware.steamos-media-creation.rules"
}
