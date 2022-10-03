# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=flatpak
pkgver=1.12.4
pkgrel=1.1
pkgdesc="Linux application sandboxing and distribution framework (formerly xdg-app)"
url="https://flatpak.org"
arch=(x86_64)
license=(LGPL)
depends=(dbus glib2 libsoup polkit libxau ostree json-glib libseccomp libarchive
         python bubblewrap appstream-glib xdg-dbus-proxy systemd)
makedepends=(intltool gobject-introspection gtk-doc git docbook-xsl xmlto)
checkdepends=(valgrind socat)
provides=(libflatpak.so)
_commit=103ed5c02c8453580fac19e5122d150f44f6774f  # tags/1.12.4^0
source=("git+https://github.com/flatpak/flatpak#commit=$_commit"
        git+https://gitlab.gnome.org/GNOME/libglnx.git
        git+https://github.com/projectatomic/bubblewrap
        git+https://github.com/flatpak/xdg-dbus-proxy
        git+https://gitlab.gnome.org/alexl/variant-schema-compiler.git
        https://dl.flathub.org/repo/flathub.flatpakrepo
        stop-portal-and-helper.patch
        allow-modify_ldt-in-multiarch.patch
        flatpak-bindir.sh)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '3371dd250e61d9e1633630073fefda153cd4426f72f4afa0c3373ae2e8fea03a'
            '24be4360aa48f040bc8660532305256e03c1d4779f971f026d28bc3107fb692e'
            'f0f6322318b51f9a92f35bdcf125a11cfe345518a3b9d48f9faf84189723762b'
            '1824cb4eb1cc88702cb2b9f1c55b6dfdf20fca5eab83f6e8e532099281328745')

pkgver() {
  cd flatpak
  git describe --tags | sed 's/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd flatpak

  # Stop flatpak-session-helper / flatpak-portal when the session ends
  # Remove after Flatpak > 1.14.0 is available
  patch -p1 < "$srcdir/stop-portal-and-helper.patch"

  # Allow the modify_ldt syscall when using multiarch
  # Remove after Flatpak > 1.14.0 is available
  patch -p1 < "$srcdir/allow-modify_ldt-in-multiarch.patch"

  git submodule init
  git submodule set-url bubblewrap "$srcdir/bubblewrap"
  git submodule set-url libglnx "$srcdir/libglnx"
  git submodule set-url dbus-proxy "$srcdir/xdg-dbus-proxy"
  git submodule set-url variant-schema-compiler "$srcdir/variant-schema-compiler"
  git submodule update

  # https://github.com/flatpak/flatpak/issues/267
  sed -i '/locale\/C\./d' tests/make-test-runtime.sh

  NOCONFIGURE=1 ./autogen.sh
}

build() {
  cd flatpak

  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib \
    --disable-static \
    --enable-gtk-doc \
    --with-system-bubblewrap \
    --with-system-dbus-proxy \
    --with-dbus-config-dir=/usr/share/dbus-1/system.d

  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

  make
}

check() {
  cd flatpak
  make -k check
}

package() {
  depends+=(xdg-desktop-portal)

  make -C flatpak DESTDIR="$pkgdir" install

  install -Dt "$pkgdir/etc/profile.d" -m644 flatpak-bindir.sh
  install -Dt "$pkgdir/etc/flatpak/remotes.d" flathub.flatpakrepo

  # Fixup mode to match polkit
  install -d -o root -g 102 -m 750 "$pkgdir/usr/share/polkit-1/rules.d"
}
