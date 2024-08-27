# Maintainer: Campbell Jones <serebit at archlinux dot org>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgbase=ibus
pkgname=(ibus libibus)
pkgver=1.5.30
pkgrel=1.2
pkgdesc="Intelligent input bus for Linux/Unix"
arch=('x86_64')
url="https://github.com/ibus/ibus/wiki"
license=('LGPL-2.1-or-later')
depends=(
    'at-spi2-core'
    'cairo'
    'dconf'
    'gdk-pixbuf2'
    'glib2'
    'graphene'
    'gtk3'
    'gtk4'
    'hicolor-icon-theme'
    'libdbusmenu-glib'
    'libdbusmenu-gtk3'
    'libnotify'
    'libx11'
    'libxkbcommon'
    'libxfixes'
    'libxi'
    'pango'
    'python>=3.11'
    'python<3.12'
    'python-dbus'
    'python-gobject'
    'wayland'
)
makedepends=(
    'gnome-common'
    'gobject-introspection'
    'gtk-doc'
    'intltool'
    'qt5-base'
    'unicode-character-database'
    'unicode-cldr'
    'unicode-emoji'
    'vala'
)
options=('!emptydirs')
source=("https://github.com/$pkgname/$pkgname/releases/download/$pkgver/${pkgname}-${pkgver}.tar.gz")
b2sums=('47dbcfec309bda14273463bff875e283148c7aba872d8e9f7673dd18e703f7b2a0eab5d538bd29a36525ab667b57488f4dc046bc955c1cd34edaec5b538e2bdd')

build() {
    cd ${pkgname}-${pkgver}
    ./configure \
        --prefix=/usr \
        --libexecdir=/usr/lib/ibus \
        --sysconfdir=/etc \
        --enable-dconf \
        --enable-wayland \
        --enable-gtk-doc \
        --disable-gtk2 \
        --enable-gtk4 \
        --disable-memconf \
        --enable-ui \
        --disable-python2 \
        --with-python=python3 \
        --with-ucd-dir=/usr/share/unicode/
    sed -i 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
    make
}

package_ibus() {
    depends+=("libibus=$pkgver")

    cd ibus-${pkgver}
    make DESTDIR="$pkgdir" install
    make -C src DESTDIR="$pkgdir" uninstall
    make -C bindings DESTDIR="$pkgdir" uninstall
    make DESTDIR="$pkgdir" uninstall-pkgconfigDATA
}

package_libibus() {
    pkgdesc="IBus support library"
    depends=(libg{lib,object,io}-2.0.so python-gobject)
    provides=('libibus-1.0.so')

    cd ibus-${pkgver}
    make -C src DESTDIR="$pkgdir" install
    make -C bindings DESTDIR="$pkgdir" install
    make DESTDIR="$pkgdir" install-pkgconfigDATA
}
