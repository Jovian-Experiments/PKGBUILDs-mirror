# Maintainer (Holo): Alberto Garcia <berto@igalia.com>
# Maintainer: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=flatpak
pkgver=1.14.4
pkgrel=2.1
pkgdesc="Linux application sandboxing and distribution framework (formerly xdg-app)"
url="https://flatpak.org"
arch=(x86_64)
license=(LGPL)
depends=(
  appstream
  bubblewrap
  curl
  dbus
  fuse3
  glib2
  json-glib
  libarchive
  libmalcontent
  libseccomp
  libxau
  ostree
  polkit
  python
  systemd
  xdg-dbus-proxy
)
makedepends=(
  docbook-xsl
  git
  gobject-introspection
  gtk-doc
  python-pyparsing
  xmlto
)
checkdepends=(valgrind socat)
_commit=8a1edceadfab936953e2ab947b0e7ae5b71e4173  # tags/1.14.4^0
source=("git+https://github.com/flatpak/flatpak#commit=$_commit"
        git+https://gitlab.gnome.org/GNOME/libglnx.git
        git+https://github.com/projectatomic/bubblewrap
        git+https://github.com/flatpak/xdg-dbus-proxy
        git+https://gitlab.gnome.org/alexl/variant-schema-compiler.git
        https://dl.flathub.org/repo/flathub.flatpakrepo
        allow-modify_ldt-in-multiarch.patch
        # Holo: Fix and test case for CVE-2024-32462 -- https://github.com/flatpak/flatpak/security/advisories/GHSA-phv6-cpc2-2fgj
        CVE-2024-32462-fix.patch
        CVE-2024-32462-test.patch
        # Holo: Show app name instead of developer name in 'flatpak list' -- https://github.com/flatpak/flatpak/issues/5700
        show-app-name-fix.patch
        show-app-name-test.patch
        fusermount3.diff
        flatpak-bindir.sh)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '3371dd250e61d9e1633630073fefda153cd4426f72f4afa0c3373ae2e8fea03a'
            'f0f6322318b51f9a92f35bdcf125a11cfe345518a3b9d48f9faf84189723762b'
            '410e144c08da8e9dd77a12b2d144ec8c9ceb5259554d39fee2a72228515cf82b'
            '765accd41516d0cde1df4c2447a73f553f143df99769da80ce380055e1980e6c'
            'a4d8a71b920ea81c89548f798379ae51fc48c7371d9f9a10a9e1e3c1ff82de94'
            '90cadfd4b2507bf319dd13777feefb47434fe6b70f4ead4ca5c3f4d21899ec73'
            '23e01650d60222082ffb67a16d3ea033192cc9e6932027cf0ea0c55ea17863af'
            '1824cb4eb1cc88702cb2b9f1c55b6dfdf20fca5eab83f6e8e532099281328745')

pkgver() {
  cd flatpak
  git describe --tags | sed 's/[^-]*-g/r&/;s/-/+/g'
}

prepare() {
  cd flatpak

  # Allow the modify_ldt syscall when using multiarch
  # Remove after Flatpak > 1.15.3 is available
  git apply -3 "$srcdir/allow-modify_ldt-in-multiarch.patch"

  # Support fuse3
  # https://bugs.archlinux.org/task/75623
  git apply -3 "$srcdir/fusermount3.diff"

  # Holo: Fix for CVE-2024-32462
  git apply -3 "$srcdir/CVE-2024-32462-fix.patch"
  git apply -3 "$srcdir/CVE-2024-32462-test.patch"

  # Holo: Fix for flatpak#5700
  git apply -3 "$srcdir/show-app-name-fix.patch"
  git apply -3 "$srcdir/show-app-name-test.patch"

  git submodule init
  git submodule set-url bubblewrap "$srcdir/bubblewrap"
  git submodule set-url dbus-proxy "$srcdir/xdg-dbus-proxy"
  git submodule set-url libglnx "$srcdir/libglnx"
  git submodule set-url variant-schema-compiler "$srcdir/variant-schema-compiler"
  git -c protocol.file.allow=always submodule update

  NOCONFIGURE=1 ./autogen.sh
}

build() {
  local configure_options=(
    --prefix=/usr
    --sysconfdir=/etc
    --localstatedir=/var
    --sbindir=/usr/bin
    --libexecdir=/usr/lib
    --disable-static
    --enable-docbook-docs
    --enable-gtk-doc
    --with-curl
    --with-dbus-config-dir=/usr/share/dbus-1/system.d
    --with-system-bubblewrap
    --with-system-dbus-proxy
  )

  cd flatpak
  ./configure "${configure_options[@]}"
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

check() {
  cd flatpak
  make -k check
}

package() {
  depends+=(xdg-desktop-portal libostree-1.so)
  provides=(libflatpak.so)

  make -C flatpak DESTDIR="$pkgdir" install

  install -Dt "$pkgdir/etc/profile.d" -m644 flatpak-bindir.sh
  install -Dt "$pkgdir/etc/flatpak/remotes.d" flathub.flatpakrepo

  # Fixup mode to match polkit
  install -d -o root -g 102 -m 750 "$pkgdir/usr/share/polkit-1/rules.d"
}
