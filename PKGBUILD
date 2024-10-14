# Maintainer: Bruno Pagani <archange@archlinux.org>
# Maintainer: Filipe Laíns (FFY00) <lains@archlinux.org>
# Maintainer: Frederik Schwan <freswa at archlinux dot org>
# Contributor: Mirco Tischler <mt-ml at gmx dot de>

pkgname=fwupd-minimal
pkgver=1.9.26
pkgrel=1
pkgdesc="Simple daemon to allow session software to update firmware"
arch=(x86_64)
url='https://github.com/fwupd/fwupd'
license=(LGPL-2.1-or-later)
depends=(
  bash
  bluez
  curl
  fwupd-efi
  gcc-libs
  glib2
  glibc
  gnutls
  hicolor-icon-theme
  json-glib
  libarchive
  libcbor
  libgudev
  libgusb
  libjcat
  libxmlb
  polkit
  'python>=3.11'
  'python<3.12'
  shared-mime-info
  sqlite
  systemd-libs
  xz
  zlib
)
makedepends=(
  bash-completion
  gnu-efi-libs
  libdrm
  meson
  noto-fonts
  noto-fonts-cjk
  python-cairo
  python-dbus
  python-gobject
  python-jinja
  python-pillow
  vala
  valgrind
)
checkdepends=(umockdev)
source=(
  "https://github.com/fwupd/fwupd/releases/download/${pkgver}/fwupd-${pkgver}.tar.xz"{,.asc}
  fwupd.sysusers
)
sha512sums=('04684f0be26c1daec9966e62c7db103cce923bb361657c66111e085e9a388e812250ac18774ef83eac672852489acc2ab21b9d7c94a28a8e5564e8bb7d67c0ba'
            'SKIP'
            '637203080b55eda74a659f58c853a9a723a2dad5da70915b2b0e036c6145a649468ebec700cc83975d9cb5378b9dced8b3a3b26bdbcc75ddc774837355e75deb')
b2sums=('11551c22bbce26cb1e7117e76f7d02077cf22889cdf21711a4dc2e523630335efcd20cf44dffecab74c04cd3dbd0cb5faa8277e220e193e613d75c4a9353e623'
        'SKIP'
        'e65ca7da22a20a40882cfc1fe4479643f9a38c90a4f2c3e71e6e5e3de1d6db212a0f17d600097619fe3cdb0a9b860422f8b0b9a9d45441518e51a7eb12a918bb')
validpgpkeys=(163EB50119225DB3DF8F49EA17ACBA8DFA970E17) # Richard Hughes <richard@hughsie.com>

build() {
  local meson_options=(
    -D docs=disabled
    -D efi_binary=false
    -D launchd=disabled
    -D supported_build=enabled
    -D systemd_unit_user=fwupd
    -D hsi=disabled
    -D introspection=false
    -D plugin_redfish=false
    -D plugin_tpm=disabled
    -D plugin_flashrom=disabled
    -D plugin_logitech_bulkcontroller=disabled
    -D passim=disabled
    -D plugin_cpu=disabled
    -D plugin_modem_manager=disabled
    -D plugin_scsi=disabled
    -D plugin_bcm57xx=disabled
    -D plugin_redfish=disabled
    -D plugin_powerd=disabled
    -D fish_completion=false
  )

  arch-meson fwupd-${pkgver} build "${meson_options[@]}"
  meson compile -C build
}

check() {
  meson test -C build --print-errorlogs
}

_pick() {
  local p="$1" f d; shift
  for f; do
    d="$srcdir/$p/${f#$pkgdir/}"
    mkdir -p "$(dirname "$d")"
    mv "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

package() {
  depends+=(
    libarchive.so
    libcbor.so
    libcurl.so
    libgudev-1.0.so
    libjson-glib-1.0.so
  )
  optdepends=(
    'python-dbus: Firmware packaging tools'
    'python-gobject: Firmware packaging tools'
    'udisks2: UEFI firmware upgrade support'
  )
  provides=(libfwupd.so)
  backup=(
    'etc/fwupd/fwupd.conf'
    'etc/fwupd/remotes.d/lvfs-testing.conf'
    'etc/fwupd/remotes.d/lvfs.conf'
    'etc/fwupd/remotes.d/vendor-directory.conf'
  )

  meson install -C build --destdir "${pkgdir}"
  # Add fwupd user https://bugs.archlinux.org/task/79653
  install -D -m644 fwupd.sysusers "${pkgdir}"/usr/lib/sysusers.d/fwupd.conf
  # Remove the tests
  rm -r "${pkgdir}"/usr/{lib,share}/installed-tests/
  # Conflicts with the dbxtool package
  mv "${pkgdir}"/usr/bin/{,fwupd-}dbxtool
  mv "${pkgdir}"/usr/share/man/man1/{,fwupd-}dbxtool.1

}
