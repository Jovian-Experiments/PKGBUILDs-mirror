# Maintainer: Morten Linderud <foxboron@archlinux.org>
# Maintainer: David Runge <dvzrv@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Maintainer (Holo): Alberto Garcia <berto@igalia.com>

pkgbase=podman
pkgname=podman # Holo: build only podman and not podman-docker
pkgver=4.5.1
_commit=9eef30051c83f62816a1772a743e5f1271b196d7  #refs/tags/v4.5.0^{}
pkgrel=1.1
pkgdesc='Tool and library for running OCI-based containers in pods'
arch=(x86_64)
url='https://github.com/containers/podman'
license=(Apache)
makedepends=(
  apparmor
  btrfs-progs
  catatonit
  device-mapper
  git
  go
  go-md2man
  gpgme
  libseccomp
  systemd
)
# https://github.com/containers/podman/issues/13297
options=(!lto)
source=(
  git+$url#commit=$_commit?signed
  $pkgname-4.2.0-defaultinitpath.patch
)
# See the release-keys repository
# https://github.com/containers/release-keys
validpgpkeys=(
  B7DBDCA456F7335E91F1C25CD3624C551D0515C4  # Matthew Heon <mheon@redhat.com>
  7CE1E6F8C90CB53E7E4D8F2D502E08DB0BBF8EEE  # Ashley Cui <acui@redhat.com>
  9E33DD8704CC03E2DEB84D9A1C1EDD7CC7C3A0DD  # Lokesh Mandvekar <lsm5@redhat.com>
)
sha256sums=('SKIP'
            'e4d15d2cf45237ddff64d149956e9f9c0ce366bd0bdf8d98de65269f53d4885d')

pkgver() {
  cd $pkgname
  git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
  # set default init_path to /usr/lib/podman/catatonit
  # https://bugs.archlinux.org/task/75493
  # https://github.com/containers/common/issues/1110
  patch -Np1 -d $pkgname -i ../$pkgname-4.2.0-defaultinitpath.patch
}

build() {
  # NOTE: the BUILDTAGS may change over time
  export BUILDTAGS='apparmor seccomp systemd'
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie"
  export GOPATH="${srcdir}"

  # NOTE: fix silly ETCDIR (might get reverted): https://github.com/containers/podman/issues/18250
  make -j1 ETCDIR=/etc EXTRA_LDFLAGS='-compressdwarf=false -linkmode=external' PREFIX=/usr -C $pkgbase
  make docker-docs -C $pkgbase
}

package_podman() {
  depends=(
    catatonit
    conmon
    containers-common
    crun
    gcc-libs
    glibc
    iptables
    device-mapper libdevmapper.so
    gpgme libgpgme.so
    libseccomp libseccomp.so
    slirp4netns
  )
  optdepends=(
    'apparmor: for AppArmor support'
    'btrfs-progs: support btrfs backend devices'
    'cni-plugins: for an alternative container-network-stack implementation'
    'fuse-overlayfs: for storage driver in rootless environment'
    'passt: for alternative rootless network support'
    'podman-compose: for docker-compose compatibility'
    'podman-docker: for Docker-compatible CLI'
  )

  make install install.completions DESTDIR="$pkgdir" PREFIX=/usr LIBEXECDIR=/usr/lib -C $pkgbase

  # Holo: remove podman-remote, it's quite big and we don't need it
  rm -f "$pkgdir/usr/bin/podman-remote"
  rm -f "$pkgdir/usr/share/bash-completion/completions/podman-remote"
  rm -f "$pkgdir/usr/share/fish/vendor_completions.d/podman-remote.fish"
  rm -f "$pkgdir/usr/share/man/man1/podman-remote.1"
  rm -f "$pkgdir/usr/share/zsh/site-functions/_podman-remote"
}

package_podman-docker() {
  pkgdesc='Emulate Docker CLI using podman'
  depends=(
    podman
    sh
  )
  conflicts=(docker)
  provides=(docker)

  make -j1 install.docker-full DESTDIR="$pkgdir" PREFIX=/usr -C $pkgbase
}
