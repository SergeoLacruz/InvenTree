import { SimpleGrid, Text, UnstyledButton } from '@mantine/core';
import React from 'react';
import { Link } from 'react-router-dom';

import * as classes from '../../main.css';
import { DocTooltip } from './DocTooltip';

export interface MenuLinkItem {
  id: string;
  text: string | JSX.Element;
  link: string;
  highlight?: boolean;
  doctext?: string | JSX.Element;
  docdetail?: string | JSX.Element;
  doclink?: string;
  docchildren?: React.ReactNode;
}

export type menuItemsCollection = {
  [key: string]: MenuLinkItem;
};

function ConditionalDocTooltip({
  item,
  children
}: Readonly<{
  item: MenuLinkItem;
  children: React.ReactNode;
}>) {
  if (item.doctext !== undefined) {
    return (
      <DocTooltip
        key={item.id}
        text={item.doctext}
        detail={item?.docdetail}
        link={item?.doclink}
        docchildren={item?.docchildren}
      >
        {children}
      </DocTooltip>
    );
  }
  return <>{children}</>;
}

export function MenuLinks({
  links,
  highlighted = false
}: Readonly<{
  links: MenuLinkItem[];
  highlighted?: boolean;
}>) {
  const filteredLinks = links.filter(
    (item) => !highlighted || item.highlight === true
  );

  return (
    <SimpleGrid cols={2} spacing={0}>
      {filteredLinks.map((item) => (
        <ConditionalDocTooltip item={item} key={item.id}>
          <UnstyledButton
            className={classes.subLink}
            component={Link}
            to={item.link}
            p={0}
          >
            <Text size="sm" fw={500}>
              {item.text}
            </Text>
          </UnstyledButton>
        </ConditionalDocTooltip>
      ))}
    </SimpleGrid>
  );
}
