# Maintainer: Umang Jain (uajain) <uajain@igalia.com>

pkgbase=linux-neptune-618-devel
_tag=6.18.25-valve1
pkgver=${_tag//-/.}
pkgrel=1
pkgdesc='Linux'
url="https://gitlab.steamos.cloud/jupiter/linux-integration/-/tree/$_tag"
arch=(x86_64)
license=(GPL-2.0-only)
makedepends=(
  bc
  cpio
  gettext
  libelf
  pahole
  perl
  python
  tar
  xz

  # Jupiter: we're using git+ssh for the source
  git
  openssh
)
options=(
  !debug
  !strip
)
_srcname=archlinux-linux-neptune-devel
source=(
  "$_srcname::git+ssh://git@gitlab.steamos.cloud/jupiter/linux-integration.git#tag=$_tag"
  config.x86_64   # Upstream Arch Linux kernel configuration file, DO NOT EDIT!!!
  config-neptune  # Jupiter: the neptune kernel fragment file (overrides 'config.x86_64' above)
  config-neptune-devel  # Jupiter: the neptune devel kernel fragment file
)
sha256sums=('bfbdcb2253977740e39cf09215480d82eb9af216869810623a980f4193ebd986'
            'e765199f6fbafbe57d013d40e0d2918cbab30fb2a090e01eb7821a515b6b1b8a'
            '8fec943cf08cb8988da28b4829a4b192a71aef2887df48004ebb80f6e9597020'
            'a9e0f3aa421a4cd2ccc840853d52b7aaeb2e2792238e4e953d0776f0f3061bc6')

export KBUILD_BUILD_HOST=archlinux
export KBUILD_BUILD_USER=$pkgbase
export KBUILD_BUILD_TIMESTAMP="$(date -Ru${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH})"

prepare() {
  cd $_srcname

  echo "Setting version..."
  echo "-$pkgrel" > localversion.10-pkgrel
  echo "${pkgbase#linux}" > localversion.20-pkgname

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    src="${src%.zst}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  echo "Setting config..."
  cp ../config.x86_64 .config
  scripts/kconfig/merge_config.sh -m ../config.x86_64 ../config-neptune ../config-neptune-devel
  make olddefconfig
  diff -u ../config.x86_64 .config || :

  make -s kernelrelease > version
  echo "Prepared $pkgbase version $(<version)"
}

build() {
  cd $_srcname
  make all
  make -C tools/bpf/bpftool vmlinux.h feature-clang-bpf-co-re=1
}

_package() {
  pkgdesc="The $pkgdesc kernel and modules"
  depends=(
    coreutils
    initramfs
    kmod
  )
  optdepends=(
    'wireless-regdb: to set the correct wireless channels of your country'
    'linux-firmware: firmware images needed for some devices'
  )
  provides=(
    KSMBD-MODULE
    VIRTUALBOX-GUEST-MODULES
    WIREGUARD-MODULE
  )
  replaces=(
    virtualbox-guest-modules-arch
    wireguard-arch
  )

  cd $_srcname
  local modulesdir="$pkgdir/usr/lib/modules/$(<version)"

  echo "Installing boot image..."
  # systemd expects to find the kernel here to allow hibernation
  # https://github.com/systemd/systemd/commit/edda44605f06a41fb86b7ab8128dcf99161d2344
  install -Dm644 "$(make -s image_name)" "$modulesdir/vmlinuz"

  # Used by mkinitcpio to name the kernel
  echo "$pkgbase" | install -Dm644 /dev/stdin "$modulesdir/pkgbase"

  echo "Installing modules..."
  ZSTD_CLEVEL=19 make INSTALL_MOD_PATH="$pkgdir/usr" INSTALL_MOD_STRIP=1 \
    DEPMOD=/doesnt/exist modules_install  # Suppress depmod

  # remove build link
  rm "$modulesdir"/build
}

pkgname=("$pkgbase")
for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package${_p#$pkgbase}")
    _package${_p#$pkgbase}
  }"
done

# vim:set ts=8 sts=2 sw=2 et:
